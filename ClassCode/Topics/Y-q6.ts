const y: number = 1;
function bigfun() {
    const x: number = 2;

    function smallboredom(f: CallableFunction) {
        console.log(f(x));
    }

    function a(){
        const x: number =  3;
        smallboredom((y: number) => y * x);
    }

    a();
}
