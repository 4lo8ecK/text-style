#include <string>

namespace styles {
    inline std::string cd(int code = 0) {
        return "\x1b[" + std::to_string(code) + "m";
    }
    
    template<typename... Ints>
    std::string add(const std::string& text, Ints... args){
        static_assert((std::is_same_v<Ints, int> && ...), "All args must be int");
        std::string addition = "";
        ((addition += cd(args)), ...);
        return addition + text + cd(0);   
    }
    
    namespace color {
        namespace light {
            const int black   = 90;
            const int red     = 91;
            const int green   = 92;
            const int yellow  = 93;
            const int blue    = 94;
            const int purple  = 95;
            const int cyan    = 96;
            const int base   = 97;
        };
        const int base    = 0;
        const int black   = 30;
        const int red     = 31;
        const int green   = 32;
        const int yellow  = 33;
        const int blue    = 34;
        const int purple  = 35;
        const int cyan    = 36;
    };
    namespace style {
        const int base = 0;
        const int bold = 1;
        const int dim = 2;
        const int italic = 3;
        const int underline = 4;
        const int blink = 5;
        const int fast_blink = 6;
        const int reverse = 7;
        const int hidden = 8;
        const int cross = 9;
        const int double_underline = 21;
        const int thin_underline = 52;
    };
    namespace select {
        namespace light {
            const int black     = 100;
            const int red       = 101;
            const int green     = 102;
            const int yellow    = 103;
            const int blue      = 104;
            const int purple    = 105;
            const int cyan      = 106;
            const int white     = 107;
        };
        const int base      = 7;
        const int black     = 40;
        const int red       = 41;
        const int green     = 42;
        const int yellow    = 43;
        const int blue      = 44;
        const int purple    = 45;
        const int cyan      = 46;
        const int white     = 47;
    };
}